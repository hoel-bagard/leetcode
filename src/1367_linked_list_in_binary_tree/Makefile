APP := median
CC := g++
TEST_APP := test-runner

BIN_DIR := bin
INCLUDE_DIR := include
SOURCE_DIR := src
TEST_DIR := tests
OBJECT_DIR := obj
MAIN_SOURCE := main.cpp

OBJECT_PROD_DIR := $(OBJECT_DIR)/prod
OBJECT_DEBUG_DIR := $(OBJECT_DIR)/debug
OBJECT_TEST_DIR := $(OBJECT_DIR)/test

COMPILE_FLAGS := -std=c++17 -Wall -Wextra -Wconversion -Wsign-conversion -I$(INCLUDE_DIR)
LINK_FLAGS :=

CPP_HEADERS := $(wildcard $(INCLUDE_DIR)/*.hpp) $(wildcard $(INCLUDE_DIR)/**/*.hpp)
CPP_SOURCES := $(wildcard $(SOURCE_DIR)/*.cpp) $(wildcard $(SOURCE_DIR)/**/*.cpp)
CPP_TEST_SOURCES := $(filter-out $(SOURCE_DIR)/$(MAIN_SOURCE), $(CPP_SOURCES))
TEST_SOURCES := $(wildcard $(TEST_DIR)/*.cpp) $(wildcard $(TEST_DIR)/**/*.cpp)

CPP_PROD_OBJECTS := $(patsubst $(SOURCE_DIR)/%, $(OBJECT_PROD_DIR)/%, ${CPP_SOURCES:.cpp=.o})
CPP_DEBUG_OBJECTS := $(patsubst $(SOURCE_DIR)/%, $(OBJECT_DEBUG_DIR)/%, ${CPP_SOURCES:.cpp=.o})
CPP_TEST_OBJECTS := $(patsubst $(SOURCE_DIR)/%, $(OBJECT_TEST_DIR)/%, ${CPP_TEST_SOURCES:.cpp=.o})

MAIN_OBJECT := $(OBJECT_PROD_DIR)/${MAIN_SOURCE:.cpp=.o}


# Extra options
.PHONY: debug prod test build_test benchmark clean
.SILENT: clean

# Default build
all: prod

# Main builds
prod: COMPILE_FLAGS += -O3 -flto
prod: LINK_FLAGS += -O3 -flto
prod: $(BIN_DIR)/$(APP)

debug: COMPILE_FLAGS += -DDEBUG -DTEST -DSHOW -g
debug: LINK_FLAGS += -DDEBUG -g
debug: $(BIN_DIR)/$(APP)_debug

tests: COMPILE_FLAGS += -O0 -g `pkg-config --cflags gtest`
tests: LINK_FLAGS += `pkg-config --libs gtest`

benchmark: COMPILE_FLAGS += -O3 -flto
benchmark: LINK_FLAGS += -O3 -flto

# Test building
tests: build_test
	@$(BIN_DIR)/$(TEST_APP)
build_test: $(BIN_DIR)/$(TEST_APP)

# Benchmark
benchmark: COMPILE_FLAGS += -O3 -flto
benchmark: LINK_FLAGS += -O3 -flto
benchmark: $(BIN_DIR)/benchmark
	@$(BIN_DIR)/benchmark

# Code coverage
coverage:
	@mkdir -p $(BIN_DIR)/$(TEST_DIR)
	$(CC) -Iinclude -lgtest --coverage -O0 $(CPP_TEST_SOURCES) $(TEST_SOURCES) \
-o $(BIN_DIR)/$(TEST_DIR)/coverage $(TEST_LINK_FLAGS)

# Final link
$(BIN_DIR)/$(APP): $(CPP_PROD_OBJECTS)
	@echo -e ""
	@echo -e "\033[1m\033[92m### Building application\033[0m"
	@mkdir -p $(BIN_DIR)
	$(CC) $(CPP_PROD_OBJECTS) -o $@ $(LINK_FLAGS)
	@echo -e ""

$(BIN_DIR)/$(APP)_debug: $(CPP_DEBUG_OBJECTS)
	@echo -e ""
	@echo -e "\033[1m\033[92m### Linking application in DEBUG mode\033[0m"
	@mkdir -p $(BIN_DIR)
	$(CC) $(CPP_DEBUG_OBJECTS) -o $@ $(LINK_FLAGS)
	@echo -e ""

$(BIN_DIR)/$(TEST_APP): $(TEST_SOURCES) $(CPP_TEST_SOURCES)
	@echo -e ""
	@echo -e "\033[1m\033[92m### Linking tests\033[0m"
	@mkdir -p $(BIN_DIR)
	$(CC) $(COMPILE_FLAGS) -lgtest $^ -o $@ $(LINK_FLAGS)
	@echo -e ""

$(BIN_DIR)/benchmark: benchmark/main.cpp $(CPP_TEST_SOURCES)
	@echo -e ""
	@echo -e "\033[1m\033[92m### Building benchmark\033[0m"
	@mkdir -p $(BIN_DIR)
	$(CC) $(COMPILE_FLAGS) $^ -o $@ $(LINK_FLAGS)
	@echo -e ""

# Compile
$(OBJECT_PROD_DIR)/%.o: $(SOURCE_DIR)/%.cpp $(CPP_HEADERS)
	@echo -e "\033[92m### Compiling $<\033[0m"
	@mkdir -p $(dir $@)
	$(CC) $(COMPILE_FLAGS) $< -c -o $@

$(OBJECT_DEBUG_DIR)/%.o: $(SOURCE_DIR)/%.cpp $(CPP_HEADERS)
	@echo -e "\033[92m### Compiling $< in DEBUG mode\033[0m"
	@mkdir -p $(dir $@)
	$(CC) $(COMPILE_FLAGS) $< -c -o $@

# Clean
clean:
	@rm -rf $(OBJECT_DIR)
	@rm -rf $(BIN_DIR)
	@echo -e "\033[1m\033[93m### Project cleaned $<\033[0m"
	@echo -e ""
