export default (_env: any = null): any => {
  const env: any = _env ? _env : process.env;
  return {
    constants: {
      appEndPoint: env.API_ENDPOINT,
      serverHost: env.SERVER_HOST,
      jwtSecretKey: env.JWT_SECRET_KEY,
    },
    redisDb: {
      host: env.REDIS_DATABASE_HOST,
      port: parseInt(env.REDIS_DATABASE_PORT),
      index: parseInt(env.REDIS_DATABASE_INDEX),
      pubsubIndex: parseInt(env.REDIS_DATABASE_PUBSUB_INDEX),
      username: env.REDIS_DATABASE_USERNAME,
      password: env.REDIS_DATABASE_PASSWORD,
    },
    postgresDb: {
      postgresConnectionString: env.DATABASE_URL,
    },
  };
};
