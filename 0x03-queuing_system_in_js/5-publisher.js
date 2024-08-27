import redis from 'redis';
import util from 'util';

// Create Redis client
const client = redis.createClient();

// Promisify setTimeout for cleaner async operations
const setTimeoutPromise = util.promisify(setTimeout);

// Constants
const CHANNEL = 'holberton school channel';

// Handle Redis connection events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

// Function to publish messages with a delay
async function publishMessage(message, delay) {
  try {
    await setTimeoutPromise(delay);
    console.log(`About to send ${message}`);
    client.publish(CHANNEL, message);
  } catch (error) {
    console.error(`Failed to publish message: ${error.message}`);
  }
}

// Publish messages with different delays
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
