#
# module.mk
#

local_prog	:= bib3d
local_src	:= $(addprefix $(subdirectory)/,$(notdir \
                  $(wildcard $(SRC_DIR)/$(subdirectory)/*.cpp)))

# add local_prog to list of programs
# add local_src to list of sources
# compile and link elements of this module
$(eval $(call link_objects,$(local_prog),$(local_src)))
