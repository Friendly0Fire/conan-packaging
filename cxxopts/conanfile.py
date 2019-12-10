from conans import ConanFile, tools


class CxxoptsConan(ConanFile):
    name = "cxxopts"
    version = "2.2.0"
    license = "MIT License"
    author = "jarro2783"
    url = "https://github.com/jarro2783/cxxopts"
    description = "Lightweight C++ option parser library, supporting the standard GNU style syntax for options"
    topics = ("options")
    settings = "os", "compiler", "build_type", "arch"

    def source(self):
        git = tools.Git("repo")
        git.clone("https://github.com/jarro2783/cxxopts.git", branch="v2.2.0", shallow=True)

    def build(self):
        pass

    def package(self):
        self.copy("*.hpp", dst="include", src="repo/include")

