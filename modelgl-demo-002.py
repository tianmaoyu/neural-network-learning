import moderngl as gl
import moderngl_window as glw
import struct


# Create window
window_cls = glw.get_local_window_cls('pyglet')
window = window_cls(
    size=(1080, 960), fullscreen=False, title='Separate window',
    resizable=True, vsync=True, gl_version=(3, 3))
ctx = window.ctx
glw.activate_context(window, ctx=ctx)
window.clear()
window.swap_buffers()

# Window prog
prog = ctx.program(
    vertex_shader='''
    #version 330

    in vec3 in_vert;
    in vec4 in_color;

    uniform mat4 prj;

    out vec4 o_color;

    void main() {
        gl_Position = prj*vec4(in_vert.xyz, 1.0);
        o_color = in_color;
    }
    ''',
    fragment_shader='''
    #version 330

    in vec4 o_color;

    out vec4 f_color;

    void main() {
        f_color = o_color;
    }
    ''')

# Preparing
content = [
    .3, .3, -.5, 1, 0, 0, 1,
    .3, -.3, -.5, 1, 0, 0, 1,
    -.3, .3, -.4, 1, 0, 0, 1,

    .3, .4, -.5, 0, 0, 1, 1,
    .3, -.2, -.5, 0, 0, 1, 1,
    -.3, .4, -.45, 0, 0, 1, 1
]
buf = ctx.buffer(struct.pack(f'{len(content)}f', *content))
vao = ctx.vertex_array(prog, buf, 'in_vert', 'in_color')

f = 1
n = 0.1
prj = (
    1, 0, 0, 0,
    0, 1, 0, 0,
    0, 0, -(f+n)/(f-n), -1,
    0, 0, -(2*f*n)/(f-n), 0
)
vao.program['prj'] = prj

# Render loop
ctx.enable(gl.DEPTH_TEST)
while not window.is_closing:
    window.fbo.use()
    window.fbo.clear()
    vao.render()
    window.swap_buffers()