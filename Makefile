OBJDIR := build
OBJS := $(patsubst src/%.c, $(OBJDIR)/%.o, $(wildcard src/*.c))

.PHONY: makebuild
	mkdir $(OBJDIR)

all: makebuild libbench.a

$(OBJS): $(OBJDIR)/%.o : src/%.c
	@$(CC) -c $< -o $@

libbench.a: $(OBJS)
	@$(AR) crs $@ $?

# OBJDIR=build

# SRCS=$(wildcard src/*.c)
# HDRS=src/utils_*.h

# OBJS := $(patsubst src/%.c, $(OBJDIR)/%.o, $(wildcard src/*.c))

# OBJS=$(patsubst %.c,%.o,$(SRCS))

# %.o: %.c $(HDRS)
# 	$(CC) -c $< -o $@
