#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;

void rc4_encrypt(vector<int>& key, string& message, int N=256){
    vector<int> S(N);
    for(int i=0; i < N;i++){
        S[i] = i;
    }
    int j=0;
    for(int i=0; i < N; i++){
        j = (j + S[i] + key[i % key.size()]) % N;
        swap(S[i], S[j]);
    }

    int i = 0; j=0;
    vector<int> keystream;
    vector<int> ciphertext;

    for(char c : message){
        int m = (int) c;
        i = (i+1) % N;
        j = (j+S[i]) % N;
        swap(S[i], S[j]);

        int K = S[(S[i] + S[j]) % N];
        keystream.push_back(K);
        
        int cipher_byte = m ^ K;
        ciphertext.push_back(cipher_byte);
    }
    cout << "Keystream: [";
    for(size_t k = 0; k < keystream.size(); ++k) {
        cout << keystream[k] << (k == keystream.size() - 1 ? "" : ", ");
    }
    cout << "]\n";
    
    cout << "Message ASCII: [";
    for(size_t k = 0; k < message.length(); ++k) {
        cout << (int)message[k] << (k == message.length() - 1 ? "" : ", ");
    }
    cout << "]\n";
    
    cout << "Ciphertext (Decimal): [";
    for(size_t k = 0; k < ciphertext.size(); ++k) {
        cout << ciphertext[k] << (k == ciphertext.size() - 1 ? "" : ", ");
    }
    cout << "]\n";
    
    cout << "Ciphertext (Hex): [";
    for(size_t k = 0; k < ciphertext.size(); ++k) {
        cout << "0x" << hex << ciphertext[k] << (k == ciphertext.size() - 1 ? "" : ", ");
    }
    
    cout <<  "]" << dec << "\n";
     cout << "Ciphertext (Chars): ";
    for(size_t k = 0; k < ciphertext.size(); ++k) {
        if (ciphertext[k] >= 32 && ciphertext[k] <= 126) {
            cout << (char)ciphertext[k];
        } else {
            cout << ".";
        }
    }
    cout << "\n";

}
int main(){
    string message = "cybersecurity";
    vector<int> key_test = {2,4,1,7};
    cout << "========== TEST CASE: N = 10 ==========\n";
    rc4_encrypt(key_test, message, 10);
    cout << "\n";
    
}