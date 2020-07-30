Mock.mock("/auth-service/login", "post", {
    "errno": "@integer(0,1)",
    "errmsg": "@csentence(5,20)",
    "token": "@string(64)",
    "name": "@cname"
});