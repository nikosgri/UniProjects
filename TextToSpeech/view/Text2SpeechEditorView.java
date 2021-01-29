package view;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JMenuBar;
import javax.swing.JMenu;
import javax.swing.JMenuItem;

import commands.CommandsFactory;



import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

import javax.swing.JLayeredPane;
import java.awt.CardLayout;
import javax.swing.JPanel;


import com.sun.speech.freetts.Voice;
import com.sun.speech.freetts.VoiceManager;
import javax.swing.JLabel;
import java.awt.Font;





public class Text2SpeechEditorView {

	private JFrame frame;
	private CommandsFactory factory = new CommandsFactory();
	private JLayeredPane layeredPane;
	private JPanel panel,panel_1,panel_2;
	
	
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Text2SpeechEditorView window = new Text2SpeechEditorView();
					window.frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	
	public Text2SpeechEditorView() {
		initialize();
	}

	
	private void initialize() {
		frame = new JFrame();
		frame.setBounds(100, 100, 450, 300);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		JMenuBar menuBar = new JMenuBar();
		frame.setJMenuBar(menuBar);
		//ftiaxnoume ena menou kai eisagoume oti xreiazomaste
		JMenu mnNewMenu = new JMenu("menu");
		menuBar.add(mnNewMenu);
		
		//arxikopoioume thn fwnh apo to freetts
		VoiceManager vs = VoiceManager.getInstance();
		Voice talk = vs.getVoice("kevin16");
	
		
		JMenuItem mntmNewMenuItem = new JMenuItem("new Document");
		mntmNewMenuItem.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				layeredPane.removeAll();
                layeredPane.add(panel_1);
                layeredPane.repaint();
                layeredPane.revalidate();
                //kaloume tis set me8odous tis factory wste h class pou 8a kalesoume meta na exei parei ta swsta orismata
                factory.setPanel(panel_1);
                factory.setTalk(talk);
                factory.createCommand("newDoc");
				
			}
		});
		mnNewMenu.add(mntmNewMenuItem);
		
		JMenuItem mntmNewMenuItem_1 = new JMenuItem("open Document");
		mntmNewMenuItem_1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				layeredPane.removeAll();
                layeredPane.add(panel_2);
                layeredPane.repaint();
                layeredPane.revalidate();
                factory.setPanel(panel_2);
                factory.setTalk(talk);
                factory.createCommand("openDoc");
			}
		});
		mnNewMenu.add(mntmNewMenuItem_1);
		
		JMenuItem mntmNewMenuItem_2 = new JMenuItem("Audio tune");
		mntmNewMenuItem_2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent arg0) {
                factory.setTalk(talk);
                factory.createCommand("audioDoc");
                
			}
		});
		mnNewMenu.add(mntmNewMenuItem_2);
		
		
		frame.getContentPane().setLayout(null);
		
		layeredPane = new JLayeredPane();
		layeredPane.setBounds(0, 0, 434, 240);
		frame.getContentPane().add(layeredPane);
		layeredPane.setLayout(new CardLayout(0, 0));
		
		panel = new JPanel();
		layeredPane.add(panel, "name_101412562579800");
		panel.setLayout(null);
		
		JLabel lblNewLabel = new JLabel("WELCOME");
		lblNewLabel.setFont(new Font("Tahoma", Font.PLAIN, 30));
		lblNewLabel.setBounds(138, 78, 232, 59);
		panel.add(lblNewLabel);
		
		panel_1 = new JPanel();
		layeredPane.add(panel_1, "name_101414823728600");
		panel_1.setLayout(null);
		
		
		panel_2 = new JPanel();
		layeredPane.add(panel_2, "name_6850906142400");
		panel_2.setLayout(null);
		
		
		
	}
}
