// console.log("typescript")

// import moment from "moment"

// const currentTime = moment().format("YYYY MM DD")
// console.log(currentTime)

// const person: string = "muza"
// const number: number = 200

import mongoose from "mongoose";
import dotenv from "dotenv";
dotenv.config();
import app from "./app";

mongoose.connect(process.env.MONGO_URL as string, {}).then(data => {
    console.log("MONGODB connection succed");
    const PORT = process.env.PORT ?? 3003
    app.listen(PORT, function() {
        console.log(`server is run successfully on port: ${PORT}`)
    })
}).catch(err => console.log("ERROR to connect MONGODB", err));
