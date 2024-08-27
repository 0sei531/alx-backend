import redis from 'redis';

// Create Redis client
const subscriber = redis.createClient();

// Constants
const CHANNEL = 'holberton school channel';

// Handle Redis connection events
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

subscriber.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

// Subscribe to the channel
subscriber.subscribe(CHANNEL);

// Handle incoming messages
subscriber.on('message', (channel, message) => {
  if (channel === CHANNEL) {
    console.log(message);

    if (message === 'KILL_SERVER') {
      console.log('Received KILL_SERVER. Unsubscribing and quitting...');
      subscriber.unsubscribe(CHANNEL);
      subscriber.quit();
    }
  }
});
