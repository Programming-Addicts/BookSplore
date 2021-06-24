class Proxy() {
  constructor(url) {
    this.url = url
  },
    fetch(route, then_function, error_function, request_body) {
      return fetch(route, request_body).then(then_function).catch(error_function)
    }
}
