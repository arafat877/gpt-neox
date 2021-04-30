# Copyright (c) 2021, EleutherAI contributors
# This file is based on code by the authors denoted below and has been modified from its original version.
#
# Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Pretrain GPT2"""
from megatron.neox_arguments import NeoXArgs
from megatron.training import pretrain

if __name__ == "__main__":
    # TODO remove_global_vars get NeoXArgs from command line
    neox_args = NeoXArgs.from_ymls(["configs/small.yml", "configs/local_setup.yml"])
    neox_args.build_tokenizer() #TODO remove global vars shall we initialize here?
    neox_args.initialize_tensorboard_writer()  #TODO remove global vars shall we initialize here?
    neox_args.print()
    pretrain(neox_args=neox_args)
