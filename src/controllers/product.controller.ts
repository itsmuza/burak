import { Request, Response } from "express";

import { T } from "../libs/types/common";
import Errors, { HttpCode, Message } from "../libs/Errors";
import ProductService from "../models/Product.service";
import { AdminRequest } from "../libs/types/member";
import { ProductInput } from "../libs/types/product";
import ProductModel from "../schema/Product.model";

const productService = new ProductService();

const productController: T = {};

//* SPA

//* SSR
productController.getAllProduct = async (req: AdminRequest, res: Response) => {
  try {
    const result = await productService.getAllProducts();
    console.log("data:", result);
    res.render("products", { products: result });
  } catch (err) {
    if (err instanceof Errors) res.status(err.code).json(err);
    else res.status(Errors.standard.code).json(Errors.standard);
  }
};

productController.createNewProduct = async (
  req: AdminRequest,
  res: Response,
) => {
  try {
    if (!req.files?.length)
      throw new Errors(HttpCode.INTERNAL_SERVER_ERROR, Message.CREATE_FAILED);

    const data: ProductInput = req.body;
    data.productImages = req.files?.map((ele) => ele.path.replace(/\\/g, "/"));
    await productService.createNewProduct(data);
    res.send(
      `<script> alert("Sucessful creation!"); window.location.replace('admin/product/all')</script>`,
    );
  } catch (err) {
    const message =
      err instanceof Errors ? err.message : Message.SOMETHING_WENT_WRONG;
    res.send(
      `<script> alert("${message}"); window.location.replace('admin/product/all')</script>`,
    );
  }
};

productController.updateChosenProduct = async (req: Request, res: Response) => {
  try {
    const id = req.params.id as string;
    const result = await productService.updateChosenProduct(id, req.body);
    res.status(HttpCode.OK).json({ data: result });
  } catch (err) {
    if (err instanceof Errors) res.status(err.code).json(err);
    else res.status(Errors.standard.code).json(Errors.standard);
  }
};

export default productController;
