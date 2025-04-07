// src/components/ChatBox.jsx
import React, { useState, useRef, useEffect } from 'react';
import { FiSend } from 'react-icons/fi';
import axios from 'axios';
import './cb.css';
import Header from './NavBar';
import Footer from './Footer';
import { Text } from '../api/ChatBot';

const ChatBox = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  // Auto-scroll to bottom when messages update
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim() || loading) return;

    try {
      setLoading(true);

      // Add user message
      setMessages((prev) => [
        ...prev,
        {
          text: input,
          isBot: false,
          timestamp: new Date().toISOString(),
        },
      ]);

      // Get bot response
      const response = await Text(input);

      // Add bot message
      setMessages((prev) => [
        ...prev,
        {
          text: response.response, // <-- FIXED LINE
          isBot: true,
          timestamp: new Date().toISOString(),
        },
      ]);
    } catch (error) {
      console.error('Chat error:', error);
      setMessages((prev) => [
        ...prev,
        {
          text:
            error?.response?.data?.error ||
            "Sorry, I'm having trouble responding. Please try again.",
          isBot: true,
          timestamp: new Date().toISOString(),
        },
      ]);
    } finally {
      setInput('');
      setLoading(false);
    }
  };

  return (
    <>
      <Header />
      <div className="chat-container">
        <div className="messages">
          {messages.map((message, index) => (
            <div
              key={index}
              className={`message ${message.isBot ? 'bot' : 'user'}`}
            >
              <div className="message-content">
                {message.text.split('\n').map((line, i) => (
                  <p key={i}>{line}</p>
                ))}
              </div>
            </div>
          ))}
          <div ref={messagesEndRef} />
        </div>

        <form onSubmit={handleSubmit} className="input-area">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type your message..."
            disabled={loading}
          />
          <button type="submit" disabled={loading}>
            {loading ? 'Sending...' : <FiSend />}
          </button>
        </form>
      </div>
      <Footer />
    </>
  );
};

export default ChatBox;
