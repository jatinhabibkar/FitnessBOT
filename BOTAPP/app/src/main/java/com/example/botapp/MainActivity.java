package com.example.botapp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.webkit.WebSettings;
import android.webkit.WebView;


public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.webview);

        WebView myWebView = (WebView) findViewById(R.id.webview);
        WebSettings ws = myWebView.getSettings();
        ws.setJavaScriptEnabled(true);
        myWebView.loadUrl("http://ip:5000/");
    }
}