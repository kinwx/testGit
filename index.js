import dotenv from 'dotenv';
import { app } from './app.js';
import { read_root } from './routes/read_root.js';
import { get_items } from './routes/get_items.js';

dotenv.config();
// asdlnkasdnoikasd
app.use(read_root);


