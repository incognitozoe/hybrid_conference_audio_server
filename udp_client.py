package com.example.a8803hc;

import android.media.AudioFormat;
import android.media.AudioManager;
import android.media.AudioTrack;
import android.os.Environment;
import android.util.Log;

import java.io.BufferedInputStream;
import java.io.DataInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;
import java.net.UnknownHostException;

class DoNetwork  implements Runnable {

    private final DatagramSocket socket;
    private InetAddress address;
    private byte[] buf = new byte[256];
    public DoNetwork(int port) throws SocketException, UnknownHostException {
        socket = new DatagramSocket(port);
        address = InetAddress.getByName("10.0.0.234");
    }
    public void run() {
        String msg = "Hello";
        buf = msg.getBytes();
        DatagramPacket packet
                = new DatagramPacket(buf, buf.length, address, 9610);
        try {
            socket.send(packet);
        } catch (IOException e) {
            e.printStackTrace();
        }
        packet = new DatagramPacket(buf, buf.length);
        try {
            socket.receive(packet);
        } catch (IOException e) {
            e.printStackTrace();
        }
        String received = new String(
                packet.getData(), 0, packet.getLength());
        System.out.println(received+"\n");
        socket.close();
//        boolean running = true;
//
//        while (running) {
//            DatagramPacket packet
//                    = new DatagramPacket(buf, buf.length);
//            try {
//                socket.receive(packet);
//            } catch (IOException e) {
//                e.printStackTrace();
//            }
//
//            InetAddress address = packet.getAddress();
//            int port = packet.getPort();
//            packet = new DatagramPacket(buf, buf.length, address, port);
//            String received
//                    = new String(packet.getData(), 0, packet.getLength());
//
//            if (received.equals("end")) {
//                running = false;
//                continue;
//            }
//            Log.e("data", String.valueOf(received));
//        }
//        socket.close();
    }
//    public String sendEcho(String msg) throws IOException {
//        buf = msg.getBytes();
//        DatagramPacket packet
//                = new DatagramPacket(buf, buf.length, address, 9610);
//        socket.send(packet);
//        packet = new DatagramPacket(buf, buf.length);
//        socket.receive(packet);
//        String received = new String(
//                packet.getData(), 0, packet.getLength());
//        return received;
//    }

//    public void close() {
//        socket.close();
//    }
//            int p = Integer.parseInt(port.getText().toString());
//        int p=9610;
////        MediaPlayer mp1 = MediaPlayer.create(MainActivity, R.raw.test1);
//        Log.e("p: ", String.valueOf(p));
//        InetAddress hostname = null;
//        try {
////            hostname = InetAddress.getLocalHost();
////            hostname=InetAddress.getByName("localhost");
//            hostname=InetAddress.getByName("192.168.0.100");
//            Log.e("hn",String.valueOf(hostname));
//        } catch (UnknownHostException e) {
//            e.printStackTrace();
//        }
//        try {
////            Socket socket = new Socket(hostname, p);
//            Socket socket=new Socket();
//            SocketAddress socketAddress=new InetSocketAddress(hostname, p);
//            socket.connect(socketAddress);
//            InputStream input = socket.getInputStream();
//            InputStreamReader reader = new InputStreamReader(input);
//
//            int character;
//            StringBuilder data = new StringBuilder();
//
//            while ((character = reader.read()) != -1) {
//                data.append((char) character);
//            }
//
//            Log.e("data", String.valueOf(data));
//            //now send a message to the server and then read back the response.
//            try {
//
////                play();
//            } catch(Exception e) {
////                    mkmsg("Error happened sending/receiving\n");
//
//            } finally {
////                in.close();
////                out.close();
//                socket.close();
//            }
//
//        } catch (Exception e) {
////                mkmsg("Unable to connect...\n");
//        }
//    }



    public void play() {
// Get the file we want to playback.
        File file = new File(Environment.getExternalStorageDirectory().getAbsolutePath() + "/reverseme.pcm");

        // Get the length of the audio stored in the file (16 bit so 2 bytes per short)
// and create a short array to store the recorded audio.
        int musicLength = (int)(file.length()/2);
        short[] music = new short[musicLength];


        try {
// Create a DataInputStream to read the audio data back from the saved file.
            InputStream is = new FileInputStream(file);
            BufferedInputStream bis = new BufferedInputStream(is);
            DataInputStream dis = new DataInputStream(bis);

// Read the file into the music array.
            int i = 0;
            while (dis.available() > 0) {
                music[musicLength-1-i] = dis.readShort();
                i++;
            }


// Close the input streams.
            dis.close();


// Create a new AudioTrack object using the same parameters as the AudioRecord
// object used to create the file.
            AudioTrack audioTrack = new AudioTrack(AudioManager.STREAM_MUSIC,
                    11025,
                    AudioFormat.CHANNEL_CONFIGURATION_MONO,
                    AudioFormat.ENCODING_PCM_16BIT,
                    musicLength,
                    AudioTrack.MODE_STREAM);
// Start playback
            audioTrack.play();

// Write the music buffer to the AudioTrack object
            audioTrack.write(music, 0, musicLength);


        } catch (Throwable t) {
            Log.e("AudioTrack","Playback Failed");
        }
    }
}
