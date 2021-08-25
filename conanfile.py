from conans import ConanFile, CMake, tools

class Linuxdeployqt(ConanFile):
    name = "linuxdeployqt"
    version = "develop"
    license = "LICENSE.GPLv3", "LICENSE.LGPLv3"
    url = "http://172.27.128.201:8090/troila-c/linuxdeployqt"
    description = "linux platforms qt app deploy tool"
    settings = "os", "compiler", "build_type", "arch"
    generators = [("cmake"), ("cmake_find_package"), ("qt"), ("pkg_config"), ("virtualrunenv")]
    build_policy = "always"

    def export_sources(self):
        self.copy("*", dst="linuxdeployqt.AppDir", src="linuxdeployqt.AppDir")
        self.copy("*", dst="tools", src="tools")
        self.copy("*", dst="tests", src="tests")
        self.copy("*", dst="src", src="src")
        self.copy("*", dst=".git", src=".git")
        self.copy("CMakeLists.txt")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("linuxdeployqt", dst="bin", src="bin")

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")
        self.copy('*.so*', dst='bin', src='lib')
    
    def configure(self):
        self.options["qt"].shared= True
        self.options["qt"].qtsvg = True
        self.options["qt"].qtdeclarative = True
        self.options["qt"].qttools= True
        
    def requirements(self):
        self.requires("qt/5.15.2")
        self.requires("openssl/1.1.1k")
