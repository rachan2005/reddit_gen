cmake_minimum_required(VERSION 3.10)

# Project name
project(RedditGen NONE)

# Define the parent directory of the source directory
set(PARENT_DIR ${CMAKE_SOURCE_DIR}/..)

# Create directories
file(MAKE_DIRECTORY ${PARENT_DIR}/BackgroundVideos)
file(MAKE_DIRECTORY ${PARENT_DIR}/OutputVideos)
file(MAKE_DIRECTORY ${PARENT_DIR}/Screenshots)
file(MAKE_DIRECTORY ${PARENT_DIR}/Voiceovers)

# Add a custom target to run commands
add_custom_target(
    RunCommands ALL
    COMMAND ${CMAKE_COMMAND} -E echo "Running commands from CMakeLists.txt"
    COMMAND ${CMAKE_COMMAND} -E echo "Creating folders: BackgoundVideos, OutputVideos, Screenshots, Voiceovers"
    COMMAND ${CMAKE_COMMAND} -E make_directory ${PARENT_DIR}/BackgoundVideos
    COMMAND ${CMAKE_COMMAND} -E make_directory ${PARENT_DIR}/OutputVideos
    COMMAND ${CMAKE_COMMAND} -E make_directory ${PARENT_DIR}/Screenshots
    COMMAND ${CMAKE_COMMAND} -E make_directory ${PARENT_DIR}/Voiceovers
    COMMAND ${CMAKE_COMMAND} -E echo "Folders created successfully"
    COMMAND ${CMAKE_COMMAND} -E echo "Duplicating config.example.ini to config.ini"
    COMMAND ${CMAKE_COMMAND} -E echo "Source: ${CMAKE_SOURCE_DIR}/config.example.ini"
    COMMAND ${CMAKE_COMMAND} -E echo "Destination: ${PARENT_DIR}/config.ini"
    COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_SOURCE_DIR}/config.example.ini ${PARENT_DIR}/config.ini
    COMMAND ${CMAKE_COMMAND} -E echo "File duplicated successfully"
)
