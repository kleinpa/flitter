load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    sha256 = "b6d46438523a3ec0f3cead544190ee13223a52f6a6765a29eae7b7cc24cc83a0",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.1.0/rules_python-0.1.0.tar.gz",
)

load("@rules_python//python:pip.bzl", "pip_install")

pip_install(
    name = "my_deps",
    requirements = "//:requirements.txt",
)

http_archive(
    name = "com_github_kleinpa_kbtb",
    sha256 = "ae83685842e7004999dde6d6ec56eefb7364d43b6ea9c6009c1bee73dbe78131",
    strip_prefix = "kbtb-961ec507984ec8dabf2fda750ff9c068b331a2db",
    url = "https://github.com/kleinpa/kbtb/archive/961ec507984ec8dabf2fda750ff9c068b331a2db.tar.gz",
)

load("@com_github_kleinpa_kbtb//kbtb:repos.bzl", "kbtb_repos")

kbtb_repos()

load("@com_github_kleinpa_kbtb//kbtb:deps.bzl", "kbtb_deps")

kbtb_deps()

# work around: no such target '//external:python_headers'
bind(
    name = "python_headers",
    actual = "//:dummy",
)
