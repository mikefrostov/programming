// https://habr.com/ru/company/otus/blog/532582/


// app.ts
import { Application, Router, Status } from "https://deno.land/x/oak/mod.ts";

import { DatabaseController } from "./controllers/Database.ts";
import { UserRoutes } from "./routers/UserRoute.ts";

// Initialise app
const app = new Application();

// Initialise router
const router = new Router();

// Create first default route
router.get("/", (ctx) => {
    ctx.response.status = Status.OK;
    ctx.response.body = { message: "It's work !" };
});

const userRoutes = UserRoutes(router);

app.use(router.routes());
app.use(router.allowedMethods());

app.use(userRoutes.routes());
app.use(userRoutes.allowedMethods());

await new DatabaseController().initModels();
console.log("? Deno start !");
await app.listen("0.0.0.0:3001");