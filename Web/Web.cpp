// Web.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include "mongoose.h"
#include <map>
#include <string>
#include <functional>
#include "mongoose.h"  

static int event_handler(struct mg_connection *conn) {
	std::cout << "enter handle" << std::endl;
	mg_send_header(conn, "test success", ("test success"));
	mg_send_data(conn, "test success", strlen("test success"));
	return 0;
}

int _tmain(int argc, _TCHAR* argv[]) {
	struct mg_server *server = mg_create_server(NULL);
	mg_set_option(server, "document_root", ".");      // Serve current directory  
	mg_set_option(server, "listening_port", "80");  // Open port 8080  
	mg_add_uri_handler(server, "/hello", event_handler);
	for (;;) {
		mg_poll_server(server, 1000);   // Infinite loop, Ctrl-C to stop  
	}
	mg_destroy_server(&server);

	return 0;
}