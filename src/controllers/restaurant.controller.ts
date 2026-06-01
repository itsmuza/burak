import { Request, Response } from "express";
import {T} from "../libs/types/common";
import MemberService from "../models/Member.service";

const restaurantController: T = {};

restaurantController.goHome = (req: Request, res: Response) => {
    try {
        res.send("Home Page");
    } catch (err) {
        console.log("Error, goHome:", err)
    }
}

restaurantController.getLogin = (req: Request, res: Response) => {
    try {
        res.send("Login Page");
    } catch (err) {
        console.log("Error, Login:", err)
    }
}

restaurantController.getSignup = (req: Request, res: Response) => {
    try {
        res.send("Signup Page");
    } catch (err) {
        console.log("Error, Signup:", err)
    }
}

restaurantController.processLogin = (req: Request, res: Response) => {
    try {
        res.send("processLogin");
    } catch (err) {
        console.log("Error, processLogin:", err)
    }
}

restaurantController.processSignup = (req: Request, res: Response) => {
    try {
        res.send("processSignup");
    } catch (err) {
        console.log("Error, processSignup:", err)
    }
}

export default restaurantController;