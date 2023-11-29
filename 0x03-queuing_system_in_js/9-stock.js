const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const app = express();
const port = 1245;

const client = redis.createClient();

const listProducts = [
  { itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4
   },
  { itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10
  },
  { itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2
  },
  { itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5
  },
];

const reserveStockById = async (itemId, stock) => {
  const setAsync = promisify(client.set).bind(client);
  await setAsync(`item.${itemId}`, stock);
};

const getCurrentReservedStockById = async (itemId) => {
  const getAsync = promisify(client.get).bind(client);
  const reservedStock = await getAsync(`item.${itemId}`);
  return reservedStock ? parseInt(reservedStock) : 0;
};

const getItemById = (id) => listProducts.find((item) => item.itemId === id);

app.get('/list_products', (req, res) => {
  const formattedProducts = listProducts.map((product) => ({
    itemId: product.itemId,
    itemName: product.itemName,
    price: product.price,
    initialAvailableQuantity: product.initialAvailableQuantity,
  }));
  res.json(formattedProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const currentQuantity = item.initialAvailableQuantity - (
    await getCurrentReservedStockById(itemId));

  res.json({
    itemId: item.itemId,
    itemName: item.itemName,
    price: item.price,
    initialAvailableQuantity: item.initialAvailableQuantity,
    currentQuantity: currentQuantity,
  });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  const currentQuantity = item.initialAvailableQuantity - (
    await getCurrentReservedStockById(itemId));

  if (currentQuantity <= 0) {
    return res.json({ status: 'Not enough stock available', itemId: itemId });
  }

  await reserveStockById(itemId, currentQuantity - 1);

  res.json({ status: 'Reservation confirmed', itemId: itemId });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

