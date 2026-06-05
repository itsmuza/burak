import mongoose from "mongoose";
import dotenv from "dotenv";
dotenv.config();
import app from "./app";

mongoose
  .connect(process.env.MONGO_URL as string, {})
  .then((data) => {
    console.log("MONGODB connection succed");
    const PORT = process.env.PORT ?? 3003;
    app.listen(PORT, function () {
      console.log(`server is run successfully on port: ${PORT}`);
      console.info(`Admin project on https://localhost:${PORT}/admin\n`);
    });
  })
  .catch((err) => console.log("ERROR to connect MONGODB", err));
