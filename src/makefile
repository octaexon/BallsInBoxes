###############################################################################
# MAKEFILE
###############################################################################

# top-level makefile
# 
# employs non-recursive make strategy


###############################################################################
# MODEL-SPECIFIC TAGS
###############################################################################

# from the perspective of the binary tree, this the relative path to the
# makescript that calls this makefile
MAKESCRIPT	:= 
# from the perspective of the binary tree/tar repo, the relative path to the
# source directory
SRC_DIR 	:= 

# ensure that this makefile is not run from within source directory
$(if $(filter $(notdir $(SRC_DIR)),$(notdir $(CURDIR))),\
       $(error Please run the makefile from the binary tree.))

# header file directory
INC_DIR 	:= $(SRC_DIR)/include


# specify where to look for files, whereafter make can use relative paths
vpath %.cpp $(SRC_DIR)
vpath %.h   $(INC_DIR)


#TAR_FILE 	:= model
#TAR_EXT		:= tar



###############################################################################
###############################################################################




###############################################################################
# COMMAND ALIASES
###############################################################################


###############################################################################
###############################################################################




###############################################################################
# HELPER FUNCTIONS
###############################################################################

# converts a list of source files to a corresponding list of object files
# $(call source_to_object,source_file_list)
source_to_object = $(subst .cpp,.o,$1)

# converts a list of object files to a corresponding list of dependency files
# $(call object_to_dependency,object_file_list)
object_to_dependency = $(subst .o,.d,$1)


# returns the subdirectory wherein the current makefile lies
# $(subdirectory)
subdirectory = $(patsubst $(SRC_DIR)/%/module.mk,%,$(lastword $(MAKEFILE_LIST)))

# $(call link_objects,program_name,source_file_list)
define link_objects
programs	+= $1
sources 	+= $2

$1 : $(call source_to_object,$2)
	@echo "\n\033[0;36mLinking object files\033[0m ------------> \033[0;33m$$@\033[0m\n"
	@$(LINK_OBJ) $$^ -o $$@
endef

###############################################################################
###############################################################################





###############################################################################
# INFORMATION COLLECTION
###############################################################################

# initialize as immediate variables
# these will be populated once include directives are invoked
programs	:=
#libraries	:=
sources		:= 
# modules containing implementation file
modules		:= modules/module_3d




# these are lazily initialized and so, when referenced, they will have an
# up-to-date value
objects			= $(call source_to_object,$(sources))
dependencies	= $(call object_to_dependency,$(objects))


###############################################################################
###############################################################################




###############################################################################
# SETUP
###############################################################################

#ifneq "$(MAKECMDGOALS)" "tar"
create_output_directories := $(shell for f in $(modules);                 \
                                     do                                   \
                                         test -d $$f || mkdir -p $$f;     \
                                     done)
#endif


# specify where to place dependency files
#dep_dir				:= .dep
# ensure it exists
#$(shell mkdir -p $(dep_dir) >/dev/null)


# compiler and linker options
CC  				:= g++-4.8
STANDARD 			:= -std=c++11
OPT_LEVEL			:= -O2

DEBUG 				:= -g
WARNINGS			:= -Wall -Wextra

DEPFLAGS			+= -MT $@ -MMD -MP -MF $*.tmpd 
CPPFLAGS 			+= $(addprefix -I ,$(INC_DIR))
CFLAGS				+= $(STANDARD) $(WARNINGS) $(OPT_LEVEL) -c

LDFLAGS 			+= $(STANDARD) $(WARNINGS) $(OPT_LEVEL)


COMPILE_SRC			= $(CC) $(DEPFLAGS) $(CFLAGS) $(CPPFLAGS)
POSTCOMPILE 		= mv -f $*.tmpd $*.d
LINK_OBJ			= $(CC) $(LDFLAGS)

# files excluded from tar
#TAR_EXCLUDED 		:= --exclude='.gitignore' --exclude='.DS_Store' \
					   --exclude='.ycm*'

###############################################################################
###############################################################################




###############################################################################
# TARGETS
###############################################################################


# default target should be specified before include directives, just in case the
# included files contain targets
.PHONY : all
all :

include $(patsubst %,$(SRC_DIR)/%/module.mk,$(modules))

all : $(programs)

%.o : %.cpp %.d
	@echo "\n\033[0;36mCompiling\033[0m <----------------------- $<"
	@echo   "         \\-----------------------> \033[0;33m$@\033[0m"
	@$(COMPILE_SRC) $< -o $@
	@$(POSTCOMPILE)

%.d : ;

ifneq "$(MAKECMDGOALS)" "clean"
-include $(patsubst %,%.d,$(basename $(sources)))
endif

.PHONY : clean
clean :
	@echo "\033[0;36mCleaning binary tree:\033[0m \c"
	@-rm -f $(programs) $(objects) $(dependencies)
	@echo "\033[0;32mdone\033[0m"


#.PHONY : tar
#tar :
#	$(eval TAR_FILE = $(TAR_FILE)$(shell date +'_%Y_%m_%d_%H_%M_%S').$(TAR_EXT))
#	@tar -cvf $(TAR_FILE) $(TAR_EXCLUDED) $(MAKESCRIPT) $(SRC_DIR)

###############################################################################
###############################################################################
