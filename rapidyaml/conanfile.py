from conans import ConanFile, tools, CMake


class RapidyamlConan(ConanFile):
    name = "rapidyaml"
    version = "0.3"
    license = "MIT License"
    author = "Joao Paulo Magalhaes dev@jpmag.me"
    url = "https://github.com/biojppm/rapidyaml"
    description = "ryml is a library to parse and emit YAML, and do it fast"
    topics = ("yaml")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def source(self):
        git = tools.Git("repo")
        git.clone("https://github.com/biojppm/rapidyaml.git", branch="master", shallow=True)
        git.run("submodule update --init --recursive")

    def build(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.configure(source_folder="repo", build_folder="build")
        cmake.build()

    def package(self):
        self.copy("*.hpp", dst="include", src="repo/src")
        self.copy("*.hpp", dst="include", src="repo/extern/c4core/src")
        self.copy("*.h", dst="include", src="repo/extern/c4core/extern")
        self.copy("*ryml.lib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["ryml"]

