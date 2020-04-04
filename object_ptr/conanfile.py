from conans import ConanFile, tools, CMake


class ObjectptrConan(ConanFile):
    name = "object_ptr"
    version = "1.0"
    license = "Boost Software License"
    author = "Anthony Williams anthony@justsoftwaresolutions.co.uk"
    url = "https://github.com/anthonywilliams/object_ptr"
    description = "an implementation of a class similar to std::experimental::observer_ptr from the Library Fundamentals TS v2, but with various improvements suggested in WG21 email discussions of the feature"
    topics = ("object_ptr")
    settings = "os", "compiler", "build_type", "arch"

    def source(self):
        git = tools.Git("repo")
        git.clone("https://github.com/anthonywilliams/object_ptr.git", branch="master", shallow=True)

    def build(self):
        pass

    def package(self):
        self.copy("*.hpp", dst="include", src="repo")

