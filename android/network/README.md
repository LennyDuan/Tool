Thanks to the blog https://www.varvet.com/blog/kotlin-with-volley/

---

#### This is the HTTP request code-packing based on Volley 
##### Useage: In a Android App (Kotlin), use this to setup Volley Network service
val service = ServiceVolley()
val apiController = APIController(service)
##### Use below code to do HTTP get/post/delete request
       apiController.get(url) { response -> //code}
       apiController.post(url, params) {}
       apiController.delete(url) {}


