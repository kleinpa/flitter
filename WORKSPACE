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
    name = "com_github_kleinpa_keyboardtoolbox",
    sha256 = "9856d191584e5b4292d02d8b1193250defb401df14b866c0f536bf0273aa859d",
    strip_prefix = "keyboard-toolbox-37420006b523643a2b69f3fc48997137fcf675da",
    url = "https://github.com/kleinpa/keyboard-toolbox/archive/37420006b523643a2b69f3fc48997137fcf675da.tar.gz",
)

load("@com_github_kleinpa_keyboardtoolbox//kbtb:repos.bzl", "kbtb_repos")

kbtb_repos()

load("@com_github_kleinpa_kicadbazel//:repos.bzl", "kicadbazel_repos")

kicadbazel_repos()

load("@com_github_kleinpa_keyboardtoolbox//kbtb:deps.bzl", "kbtb_deps")

kbtb_deps()

# work around: no such target '//external:python_headers'
bind(
    name = "python_headers",
    actual = "//:dummy",
)
