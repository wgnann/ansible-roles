const Applet = imports.ui.applet;
const GLib = imports.gi.GLib;

class BrightnessApplet extends Applet.IconApplet {
    constructor(orientation, panelHeight, instanceId) {
        super(orientation, panelHeight, instanceId);

        this.set_applet_icon_symbolic_name("sunny");
        this.set_applet_tooltip(_("Controle de brilho"));
    }

    on_applet_clicked() {
        let path = "/usr/share/cinnamon/applets/brightness@ime.usp.br/brightness.py";
        if (GLib.file_test(path, GLib.FileTest.EXISTS)) {
            GLib.spawn_command_line_async("/usr/bin/python3 " + path);
        }
        else {
            GLib.spawn_command_line_async("/usr/bin/zenity --error --text 'Arquivo não encontrado!'");
        }
    }
}

function main(metadata, orientation, panelHeight, instanceId) {
    return new BrightnessApplet(orientation, panelHeight, instanceId);
}
