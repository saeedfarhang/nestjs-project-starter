import { NestFactory } from "@nestjs/core";
import { SwaggerModule, DocumentBuilder } from "@nestjs/swagger";
import { AppModule } from "./app.module";

async function bootstrap() {
  const app = await NestFactory.create(AppModule);

  if (process.env.ENV === "development" || process.env.ENV === "local_dev") {
    const config = new DocumentBuilder()
      .setTitle("{title}")
      .setDescription("backend api document for {title} site.")
      .setVersion("1.0")
      .addBearerAuth(
        { type: "http", scheme: "bearer", bearerFormat: "JWT" },
        "access-token"
      )
      .build();
    const document = SwaggerModule.createDocument(app, config);
    SwaggerModule.setup("doc", app, document);
  }

  console.log("env: ", process.env.ENV);

  await app.listen(process.env.SERVICE_PORT);
  console.log(
    `server started at ${process.env.SERVER_HOST}:${process.env.SERVICE_PORT} 🚀🚀`
  );
}
bootstrap();
