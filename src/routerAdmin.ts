import express from "express";
const routerAdmin = express.Router();
import restaurantController from "./controllers/restaurant.controller";
import productController from "./controllers/product.controller";
import makeUploader from "./libs/utils/uploader";

routerAdmin.get("/", restaurantController.goHome);

//& login
routerAdmin
  .get("/login", restaurantController.getLogin)
  .post("/login", restaurantController.processLogin);

//& signup
routerAdmin
  .get("/signup", restaurantController.getSignup)
  .post(
    "/signup",
    makeUploader("members").single("memberImage"),
    restaurantController.processSignup,
  );

//& logout
routerAdmin.get("/logout", restaurantController.logout);

//& check-me
routerAdmin.get("/check-me", restaurantController.checkAuthSession);

//& Produc
routerAdmin.get(
  "/product/all",
  restaurantController.verifyRestaurant,
  productController.getAllProduct,
);
routerAdmin.post(
  "/product/create",
  restaurantController.verifyRestaurant,
  makeUploader("products").array("productImages", 2),
  productController.createNewProduct,
);
routerAdmin.post(
  "/product/:id",
  restaurantController.verifyRestaurant,
  productController.updateChosenProduct,
);

//& User
routerAdmin.get(
  "/user/all",
  restaurantController.verifyRestaurant,
  restaurantController.getUsers,
);

export default routerAdmin;
