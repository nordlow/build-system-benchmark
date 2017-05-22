OBJDIR := build
OBJS := $(patsubst src/%.c, $(OBJDIR)/%.o, $(wildcard src/*.c))

all: libbench.a

$(OBJS): $(OBJDIR)/%.o : src/%.c
	@$(CC) -c $< -o $@

libbench.a: $(OBJS)
	@$(AR) crs $@ $?
