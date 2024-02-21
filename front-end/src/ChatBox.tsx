const ChatBox = () => {
  return (
    <div className="flex justify-center items-end bg-gray-200 h-screen w-full">
      <div className="chat-bar flex justify-start items-center p-2 bg-white shadow-md h- rounded-lg w-full max-w-sm group mb-8">
        <input
          type="text"
          placeholder="what do you like to ask?"
          className="outline-none bg-transparent h-6 p-1 border-b-2 flex-grow mr-4 text-gray-800 hover:border-gray-300 focus:border-teal-400"
        />
        <a
          href="/"
          className="mr-3 p-1 bg-gray-200 rounded-full shadow  bg-teal-500 hover:bg-teal-800 hover:shadow-none text-white text-base"
        >
          <svg
            className="fill-current"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            width="24"
            height="24"
          >
            <path
              className="heroicon-ui"
              d="M15.6 15.47A4.99 4.99 0 0 1 7 12a5 5 0 0 1 10 0v1.5a1.5 1.5 0 1 0 3 0V12a8 8 0 1 0-4.94 7.4 1 1 0 1 1 .77 1.84A10 10 0 1 1 22 12v1.5a3.5 3.5 0 0 1-6.4 1.97zM12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"
            />
          </svg>
        </a>
        <a href="/to"></a>
      </div>
    </div>
  );
};

export default ChatBox;
