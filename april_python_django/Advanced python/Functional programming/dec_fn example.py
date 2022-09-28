def admin_permission_required(fn):
    def inner_fn(*args, **kwargs):
        user = kwargs.get("user")
        if user.role != "Admin":
            raise Exception("Permission denied")
        else:
            return fn(*args, **kwargs)


class User:
    def set_user(self, username, role):
        self.username = username
        self.role = role

    def print_details(self):
        print(self.username, self.role)


class AddCourse:
    def set_course(self, *args, **kwargs):
        self.user = kwargs.get("user")
        self.course_name = kwargs.get("course_name")

    def print_details(self):
        print(self.user, self.course_name)


class AddBatch:
    def set_batch(self, *args, **kwargs):
