cc_library(
    name = "bench",
    srcs = glob(["src/*.c", "src/*.h"]),
#   hdrs = glob(["src/*.h"]),
    linkstatic = 1,
)

action_listener(
    name = "cppcheck_c_cpp",
    mnemonics = [
        "CppCompile",
    ],
    extra_actions = [":cppcheck_echo"],
    visibility = ["//visibility:public"],
)

extra_action(
    name = "cppcheck_echo",
    cmd = "echo cppcheck_echo: $(EXTRA_ACTION_FILE)",
)
