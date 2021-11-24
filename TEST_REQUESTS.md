# TESTING REQUEST TOKENS STEPS

- Use your preferred API Client, I'll be using ThunderClient for this test.

- Send a `GET` request to `https://code401-cookie-stand-api.herokuapp.com/api/token/`.
  - If the previous step fails because `GET` is not allowed, copy and use this in your browser address bar and replace the values inside the tags `https://code401-cookie-stand-api.herokuapp.com/api/token/?username=<USERNAME>&password=<PASSWORD>`.
  - Or just manually `POST` for the credentials.

- You will recieve `refresh` and `access` tokens.

- Send a `GET` request to `https://code401-cookie-stand-api.herokuapp.com/api/v1/cookie_stands/<id>`, change the id to the item id you want to check.

- Add `Authorization` Query Parameter with the value of the `access` token.

- You will recieve a `JSON` with chips info as a response.

- You can use the `refresh` token in the same way above.
