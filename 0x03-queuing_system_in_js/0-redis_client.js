import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Unified event handlers for client connection and error handling
client.on('ready', () => {
  console.log('Redis client connected to the server');
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});
