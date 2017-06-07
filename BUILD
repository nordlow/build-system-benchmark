cc_library(
    name = "bench",
    srcs = glob(["src/*.c", "src/*.h"]),
#   hdrs = glob(["src/*.h"]),
    linkstatic = 1,
)

action_listener(
    name = "cppcheck_c_cpp",
    mnemonics = [
        "CCompile",
        "CcCompile",
        "CppCompile",
    ],
    extra_actions = [":cppcheck_cat"],
)

extra_action(
    name = "cppcheck_echo",
    cmd = "echo $(EXTRA_ACTION_FILE)",
)

extra_action(
    name = "cppcheck_cat",
    cmd = "cat $(EXTRA_ACTION_FILE)",
)
