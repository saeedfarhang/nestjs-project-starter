import { Module } from '@nestjs/common';
import { ConfigModule, ConfigService } from '@nestjs/config';
import { AuthenticationModule } from './authentication/authentication.module';
import { getEnvFilePath } from './shared/helpers/getEnvFilePath';
import configuration from '@src/configs';
import { RedisModule, RedisModuleOptions } from '@liaoliaots/nestjs-redis';
import { UserModule } from './user/user.module';
import { AuthorizationModule } from './authorization/authorization.module';
import { TokenModule } from './modules/token/token.module';
import { appProviders } from './app.provider';
import { EmailModule } from './email/email.module';
import { StudentModule } from './student/student.module';
@Module({
  imports: [
    ConfigModule.forRoot({
      isGlobal: true,
      envFilePath: getEnvFilePath(),
      load: [configuration],
    }),
    RedisModule.forRootAsync({
      imports: [ConfigModule],
      useFactory: (configService: ConfigService): RedisModuleOptions => {
        const redisConfigs = configService.get('redisDb');
        return {
          config: {
            host: redisConfigs.host,
            port: redisConfigs.port,
            db: redisConfigs.index,
          },
        };
      },
      inject: [ConfigService],
    }),
    TokenModule,
    UserModule,
    AuthenticationModule,
    AuthorizationModule,
    EmailModule,
    StudentModule,
  ],
  controllers: [],
  providers: appProviders,
})
export class AppModule {}
