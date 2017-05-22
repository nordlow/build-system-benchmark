SRCS=$(wildcard src/*.c)
HDRS=src/utils_*.h
OBJS=$(patsubst %.c,%.o,$(SRCS))

%.o: %.c $(HDRS)
	$(CC) -c $< -o $@

libbench.a : $(OBJS)
	$(AR) -cvq $@ $<
