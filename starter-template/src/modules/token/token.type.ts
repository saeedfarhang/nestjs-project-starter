export type AccessToken = string;
export type AccessTokenPayload = Record<string, any>;
export type RefreshToken = string;
export type RefreshTokenPayload = {
  userId: number;
};
