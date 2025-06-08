import Vapor
import Redis

func expireTheKey(_ key: RedisKey, redis: Vapor.Request.Redis) {
  let expireDuration = TimeAmount.seconds(30)
  _ = redis.expire(key, after: expireDuration)
}