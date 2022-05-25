
# importing pyglet module
import pyglet
# creating a window
window = pyglet.window.Window()
 
 
# video path
vidPath ="tets.mp4"
# creating a media player object
player = pyglet.media.Player()
# load the media from the source
MediaLoad = pyglet.media.load(vidPath)
# add this media in the queue
player.queue(MediaLoad)
# play the video
player.play()

# key press event    
@window.event
def on_key_press(symbol, modifier):
   
    # key "p" get press
    if symbol == pyglet.window.key.P:
        # pause the video
        player.delete()
        # printing message
        print("Video is paused")

    # key "r" get press
    if symbol == pyglet.window.key.R:
        # resume the video
        player.play()
        # printing message
        print("Video is resumed")
         
# run the pyglet application
pyglet.app.run()