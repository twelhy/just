import javax.swing.*;
import java.awt.event.*;

public class GuiApp {
    public static void main(String[] args)
    {
        JFrame frame = new JFrame("My first screen");
        JButton button = new JButton("Hello, button!");
        JLabel text = new JLabel("Hello");
        JPanel panel = new JPanel();
        JTextArea area = new JTextArea();
        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                String text = area.getText();
                JOptionPane.showMessageDialog(frame, "You writed: " + text);
            }
        });
        panel.add(text);
        panel.add(area);
        panel.add(button);
        frame.add(panel);
        frame.setSize(1280, 720);
        button.setSize(50, 30);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setVisible(true);
    }
}