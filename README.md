# myLM

---

* fork 自[LibraryManagement](https://github.com/yumendy/LibraryManagement)

* 在原本的基础上增加了 form 表单，从而用 `form.cleaned_data.get()`取代了 `request.POST.get()`，更容易实现前后端的分离

* 将数据库改用 Mysql,同时增加了对错误条件的判断