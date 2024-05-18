// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract DocumentRegistry {
    struct Document {
        bytes32 hash;
        bytes signature;
        bool valid;
        uint256 timestamp;
    }

    mapping(bytes32 => Document) private documents;

    function addDocument(bytes32 _hash, bytes memory _signature) public {
        require(_hash.length > 0, "Hash is required");
        require(_signature.length > 0, "Signature is required");
        require(documents[_hash].timestamp == 0, "Document already exists");
        require(validate(_hash, _signature), "Invalid signature");

        documents[_hash] = Document(_hash, _signature, true, block.timestamp);
    }

    function getDocument(bytes32 _hash) public view returns (Document memory) {
        require(_hash.length > 0, "Hash is required");
        require(documents[_hash].timestamp > 0, "Document not found");

        return documents[_hash];
    }

    function documentExists(bytes32 _hash) public view returns (bool) {
        require(_hash.length > 0, "Hash is required");

        return documents[_hash].timestamp > 0;
    }

    function validate(
        bytes32 _hash,
        bytes memory _signature
    ) public pure returns (bool) {
        require(_signature.length == 65, "invalid _signaturenature length");
        bytes32 r;
        bytes32 s;
        uint8 v;
        assembly {
            r := mload(add(_signature, 32))
            s := mload(add(_signature, 64))
            v := byte(0, mload(add(_signature, 96)))
        }

        address extract = ecrecover(_hash, v, r, s);
        address expected = address(0xbc56bb97DCAe27474b4bBDc2186D671BBbEC0d32);
        return extract == expected;
    }
}
