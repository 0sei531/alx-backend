import redis from 'redis';
import { promisify } from 'util';

// Create Redis client
const client = redis.createClient();

// Promisify hgetall for async/await usage
const hgetallAsync = promisify(client.hgetall).bind(client);

// Handle Redis connection events
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error.message}`);
});

// Data to store in the hash
const HASH_KEY = 'HolbertonSchools';
const schoolData = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

// Main function to store and retrieve the hash
async function main() {
  try {
    // Store each key-value pair in the hash
    for (const [key, value] of Object.entries(schoolData)) {
      await promisify(client.hset).bind(client)(HASH_KEY, key, value);
    }

    // Retrieve and display all values from the hash
    const storedData = await hgetallAsync(HASH_KEY);
    console.log(storedData);

  } catch (error) {
    console.error(`Error performing Redis operations: ${error.message}`);
  } finally {
    // Close the Redis connection
    client.quit();
  }
}

// Execute main function
main();
