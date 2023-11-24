import { Router } from "express";

const router = Router();

router.get('/items', (req, res) => {
    return res.status(200).json({Items: [1, 2, 3, 4, 5]});
});

export { router as get_items };