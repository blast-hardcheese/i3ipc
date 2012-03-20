"""
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Lesser General Public License as published by the Free
Software Foundation, either version 3 of the License, or (at your option) any
later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along
with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
from . import i3path


I3_IPCFILE = i3path.get()

I3_IPC_MAGIC = 'i3-ipc'
I3_CHUNK_SIZE = 1024
I3_SOCKET_TIMEOUT = 0.5

I3_IPC_MESSAGE_TYPE_COMMAND = 0
I3_IPC_MESSAGE_TYPE_GET_WORKSPACES = 1
I3_IPC_MESSAGE_TYPE_SUBSCRIBE = 2
I3_IPC_MESSAGE_TYPE_GET_OUTPUTS = 3

I3_IPC_REPLY_TYPE_COMMAND = 0
I3_IPC_REPLY_TYPE_WORKSPACES = 1
I3_IPC_REPLY_TYPE_SUBSCRIBE = 2
I3_IPC_REPLY_TYPE_OUTPUTS = 3

I3_IPC_EVENT_MASK = 1 << 31
I3_IPC_EVENT_WORKSPACE = I3_IPC_EVENT_MASK | 0
I3_IPC_EVENT_OUTPUT = I3_IPC_EVENT_MASK | 1

I3_IPC_MESSAGES = (I3_IPC_MESSAGE_TYPE_COMMAND,
        I3_IPC_MESSAGE_TYPE_GET_WORKSPACES,
        I3_IPC_MESSAGE_TYPE_SUBSCRIBE,
        I3_IPC_MESSAGE_TYPE_GET_OUTPUTS,)
I3_IPC_REPLIES = (I3_IPC_REPLY_TYPE_COMMAND,
        I3_IPC_REPLY_TYPE_WORKSPACES,
        I3_IPC_REPLY_TYPE_SUBSCRIBE,
        I3_IPC_REPLY_TYPE_OUTPUTS,)
I3_IPC_EVENTS = (I3_IPC_EVENT_WORKSPACE,
        I3_IPC_EVENT_OUTPUT,)
I3_IPC_ALL_REPLIES = (I3_IPC_REPLY_TYPE_COMMAND,
        I3_IPC_REPLY_TYPE_WORKSPACES,
        I3_IPC_REPLY_TYPE_SUBSCRIBE,
        I3_IPC_REPLY_TYPE_OUTPUTS,
        I3_IPC_EVENT_WORKSPACE,
        I3_IPC_EVENT_OUTPUT,)


class Events(object):
    workspace = I3_IPC_EVENT_WORKSPACE
    output = I3_IPC_EVENT_OUTPUT


class MagicKeyError(Exception):
    pass


class EventError(Exception):
    pass
