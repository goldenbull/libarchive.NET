# libarchive.NET
dotnet interop with libarchive

1. use python script in `py` folder to parse the `archive.h` and `archive_entry.h`, and generated C# files.
2. generated C# files are in `cs` folder, as a part of the C# project.
3. use CMakeLists.txt to build libarchive, and copy the binary to `cs/lib` folder.
